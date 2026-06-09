import json
import os
import subprocess
import sys

def run_skill(input_params):
    """
    SCM订单导出工具 - OpenClaw技能入口
    
    参数：
    - input_params: dict，包含配置参数
    
    返回：
    - dict，包含执行结果
    """
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        config_file = os.path.join(script_dir, 'config.json')
        
        if 'banxingConfigs' in input_params:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            config['banxingConfigs'] = input_params['banxingConfigs']
            
            if 'chimaSize' in input_params:
                config['chimaSize'] = input_params['chimaSize']
            if 'fabricWidth' in input_params:
                config['fabricWidth'] = input_params['fabricWidth']
            if 'fabricNo' in input_params:
                config['fabricNo'] = input_params['fabricNo']
            if 'fabricStyle' in input_params:
                config['fabricStyle'] = input_params['fabricStyle']
            
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
        
        main_script = os.path.join(script_dir, 'scm_order_et_export.py')
        
        result = subprocess.run(
            [sys.executable, main_script],
            cwd=script_dir,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        output = result.stdout
        error = result.stderr
        
        success = result.returncode == 0
        
        return {
            'success': success,
            'output': output,
            'error': error,
            'production_no': extract_production_no(output)
        }
    
    except Exception as e:
        return {
            'success': False,
            'output': '',
            'error': str(e),
            'production_no': None
        }

def extract_production_no(output):
    """从输出中提取生产单号"""
    lines = output.split('\n')
    for line in lines:
        if '生产单号' in line:
            parts = line.split('：')
            if len(parts) > 1:
                return parts[1].strip()
    return None

if __name__ == '__main__':
    default_params = {
        'banxingConfigs': [
            {
                'banxing': '1KN003',
                'chimaSize': '50',
                'luocha': 'R',
                'fabricWidth': 74,
                'fabricNo': 'ET算料',
                'fabricStyle': '平板',
                'customOptions': {},
                'liangtiData': {}
            }
        ]
    }
    
    result = run_skill(default_params)
    print(json.dumps(result, ensure_ascii=False, indent=2))
