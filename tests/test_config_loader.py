# Created by 954860224@qq.com
"""
配置加载器测试
"""
import pytest
import tempfile
import yaml
from pathlib import Path
from bongobot.config_loader import load_config


class TestConfigLoader:
    """配置加载器测试类"""
    
    def test_load_default_config(self):
        """测试加载默认配置"""
        config = load_config()
        
        # 检查必需的配置项
        assert "bot" in config
        assert "clicker" in config
        assert "logging" in config
        
        # 检查bot配置
        assert "idle_threshold_seconds" in config["bot"]
        assert "keys" in config["bot"]
        
        # 检查clicker配置
        assert "enabled" in config["clicker"]
        assert "confidence" in config["clicker"]
        
        # 检查logging配置
        assert "level" in config["logging"]
    
    def test_load_custom_config(self):
        """测试加载自定义配置文件"""
        # 创建临时配置文件
        custom_config = {
            "bot": {
                "idle_threshold_seconds": 10.0,
                "keys": ["x", "y", "z"]
            },
            "clicker": {
                "enabled": False,
                "confidence": 0.9
            },
            "logging": {
                "level": "DEBUG"
            }
        }
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            yaml.dump(custom_config, f, default_flow_style=False)
            temp_path = f.name
        
        try:
            config = load_config(temp_path)
            
            # 验证自定义配置被正确加载
            assert config["bot"]["idle_threshold_seconds"] == 10.0
            assert config["bot"]["keys"] == ["x", "y", "z"]
            assert config["clicker"]["enabled"] is False
            assert config["clicker"]["confidence"] == 0.9
            assert config["logging"]["level"] == "DEBUG"
            
        finally:
            Path(temp_path).unlink()
    
    def test_invalid_config_file(self):
        """测试无效配置文件处理"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write("invalid: yaml: content: [")
            temp_path = f.name
        
        try:
            # 应该回退到默认配置
            config = load_config(temp_path)
            assert config is not None
            assert "bot" in config
            
        finally:
            Path(temp_path).unlink()
    
    def test_nonexistent_config_file(self):
        """测试不存在的配置文件"""
        config = load_config("nonexistent_file.yaml")
        
        # 应该返回默认配置
        assert config is not None
        assert "bot" in config
        assert "clicker" in config
        assert "logging" in config
