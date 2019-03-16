import os


class BaseConfig:
    """Default configuration. Details from this configuration
    class are shared across all environments  """
    DEBUG = False
    TESTING = False
    SECRET = os.getenv('SECRET')
    DATABASE_URI = 'postgres://postgres:psql@localhost:5432/ireporter'


class DevelopmentConfig(BaseConfig):
    """Development configuraion. Loads development configuration data
    when the app is in the development environment"""
    DEBUG = True
    TESTING = False
    ENV = "Development"
    DATABASE_URI = 'postgres://postgres:psql@localhost:5432/ireporter'


class TestingConfig(BaseConfig):
    """Testing configuraion. Loads Test configuration data
    when the app is in the Test environment"""
    DEBUG = True
    TESTING = True
    ENV = "Testing"
    DATABASE_URI = 'postgres://postgres:psql@localhost:5432/test_ireporter'


class ProductionConfig(BaseConfig):
    """Production configuraion. Loads Production configuration data
    when the app is in the Production environment"""
    DEBUG = False
    TESTING = False
    ENV = "Production"
    DATABASE_URI = 'postgres: // nukqopkwuzghqz: 93a266aab1ef0d66b51cf47cdd06f5b5fd798d52b1f37811030ce65fced37b8f@ec2-50-19-109-120.compute-1.amazonaws.com: 5432/d2bv1ep4fasunf'



app_config = {
    "Development": DevelopmentConfig,
    "Testing": TestingConfig,
    "Production": ProductionConfig
}
