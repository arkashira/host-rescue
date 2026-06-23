from ci_cd_pipeline import CICDPipeline

def test_integrate():
    pipeline = CICDPipeline("test-pipeline", {})
    config = {"stage1": "success", "stage2": "success"}
    assert pipeline.integrate(config) == True
    assert pipeline.stages == config

def test_integrate_empty_config():
    pipeline = CICDPipeline("test-pipeline", {})
    config = {}
    assert pipeline.integrate(config) == False
    assert pipeline.stages == {}

def test_configure():
    pipeline = CICDPipeline("test-pipeline", {})
    config = {"stage1": "success", "stage2": "success"}
    assert pipeline.configure(config) == True
    assert pipeline.stages == config

def test_configure_empty_config():
    pipeline = CICDPipeline("test-pipeline", {})
    config = {}
    assert pipeline.configure(config) == False
    assert pipeline.stages == {}

def test_deploy():
    pipeline = CICDPipeline("test-pipeline", {"stage1": "success", "stage2": "success"})
    assert pipeline.deploy() == True

def test_deploy_empty_stages():
    pipeline = CICDPipeline("test-pipeline", {})
    assert pipeline.deploy() == False
