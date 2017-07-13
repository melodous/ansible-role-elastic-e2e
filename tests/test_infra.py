import pytest

def test_elastic_e2e_server_running_and_enabled(Command,Service):
  # Check that docker service is running and enabled
  docker_service = Service("docker")
  assert docker_service.is_running
  assert docker_service.is_enabled
  # Check that elastic_e2e service is running and enabled
  elastic_e2e_service = Service("elastic_e2e")
  assert elastic_e2e_service.is_running
  assert elastic_e2e_service.is_enabled

  # Check that elastic_e2e-cli ping
  elastic_e2e_output = Command.check_output("docker exec elastic_e2e elastic_e2e-cli ping")
  assert elastic_e2e_output == "PONG"

def test_elastic_e2e_start_stop(Command,Service):
  Command.run_expect([0],"systemctl stop elastic_e2e")
  elastic_e2e_service = Service("elastic_e2e")
  assert not elastic_e2e_service.is_running
  Command.run_expect([0],"systemctl start elastic_e2e")
  assert elastic_e2e_service.is_running
  Command.run_expect([0],"systemctl restart elastic_e2e")
  assert elastic_e2e_service.is_running
  elastic_e2e_output = Command.check_output("docker exec elastic_e2e elastic_e2e-cli ping")
  assert elastic_e2e_output == "PONG"
