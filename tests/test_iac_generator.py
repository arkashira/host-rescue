import pytest
from iac_generator import generate_iac_code, review_and_modify_iac_code
from iac_generator import InfrastructureConfig

def test_generate_iac_code():
    config = InfrastructureConfig("aws", {"instance_type": "t2.micro"})
    iac_code = generate_iac_code(config)
    assert "aws" in iac_code
    assert "t2.micro" in iac_code

def test_generate_iac_code_error():
    config = InfrastructureConfig(None, {"instance_type": "t2.micro"})
    with pytest.raises(ValueError):
        generate_iac_code(config)

def test_review_and_modify_iac_code():
    iac_code = '{"platform": "aws", "resources": {"instance_type": "t2.micro"}}'
    modified_iac_code = review_and_modify_iac_code(iac_code)
    assert "reviewed" in modified_iac_code
    assert "true" in modified_iac_code
