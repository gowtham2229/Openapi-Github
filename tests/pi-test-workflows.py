import schemathesis
import requests

schema = schemathesis.from_uri("http://127.0.0.1:8000/openapi.json")

@schema.parametrize()
def test_api(case):
    response = case.call()
    case.validate_response(response)


def test_workflow():
    base = "http://127.0.0.1:8000"

    # Create Task
    r = requests.post(
        f"{base}/create_tasks",
        json={"title": "test", "description": "test desc"}
    )

    assert r.status_code == 200

    task_id = r.json().get("task_id")

    assert task_id is not None

    # Update Task
    r2 = requests.put(
        f"{base}/update_task",
        json={
            "task_id": task_id,
            "title": "updated",
            "description": "updated desc"
        }
    )

    assert r2.status_code == 200

    # Delete Task
    r3 = requests.delete(
        f"{base}/delete_tasks",
        json={"task_id": task_id}
    )

    assert r3.status_code == 200