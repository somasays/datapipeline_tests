from dags import hello_world
from tests.dag_test_utilities import assert_dag_dict_equal


def test_dag_shape():
    dag = hello_world.dag
    assert_dag_dict_equal({"hello": ["world"], "world": []}, dag)
