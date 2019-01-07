import settings
import requests
import os


def get_physical_projector_data_from_logical_name(logical_projector_name):
    if logical_projector_name == "PJ1":
        return {
            "result": "succeeded",
            "logical_projector_name": "{0}".format(logical_projector_name),
            "physical_projector_ip_address": os.getenv("{0}_IP_ADDRESS".format(logical_projector_name)),
            "physical_projector_web_username": os.getenv("{0}_WEB_USERNAME".format(logical_projector_name)),
            "physical_projector_web_password": os.getenv("{0}_WEB_PASSWORD".format(logical_projector_name))
        }
    elif logical_projector_name == "PJ2":
        return {
            "result": "succeeded",
            "logical_projector_name": "{0}".format(logical_projector_name),
            "physical_projector_ip_address": os.getenv("{0}_IP_ADDRESS".format(logical_projector_name)),
            "physical_projector_web_username": os.getenv("{0}_WEB_USERNAME".format(logical_projector_name)),
            "physical_projector_web_password": os.getenv("{0}_WEB_PASSWORD".format(logical_projector_name))
        }
    elif logical_projector_name == "PJ3":
        return {
            "result": "succeeded",
            "logical_projector_name": "{0}".format(logical_projector_name),
            "physical_projector_ip_address": os.getenv("{0}_IP_ADDRESS".format(logical_projector_name)),
            "physical_projector_web_username": os.getenv("{0}_WEB_USERNAME".format(logical_projector_name)),
            "physical_projector_web_password": os.getenv("{0}_WEB_PASSWORD".format(logical_projector_name))
        }
    else:
        return {
            "result": "failed",
            "message": "",
            "message_from_kimura": "プロジェクタ名は「PJ1」「PJ2」「PJ3」のどれかを指定してください。"
        }


def set_power_on(result_dict):
    response = requests.get(
        "http://{pj_ip_address}/base_conf.htm?CTL=fon".format(pj_ip_address=result_dict["physical_projector_ip_address"]),
        auth=(result_dict["physical_projector_web_username"], result_dict["physical_projector_web_password"]))
    if response.status_code == 200:
        return {
            "result": "succeeded",
            "message": "set power on"
        }
    else:
        return {
            "result": "failed",
            "message_from_kimura": "電源ONにできませんでした。"
        }


def set_power_off(result_dict):
    response = requests.get(
        "http://{pj_ip_address}/base_conf.htm?CTL=foff".format(pj_ip_address=result_dict["physical_projector_ip_address"]),
        auth=(result_dict["physical_projector_web_username"], result_dict["physical_projector_web_password"]))
    if response.status_code == 200:
        return {
            "result": "succeeded",
            "message": "set power off"
        }
    else:
        return {
            "result": "failed",
            "message_from_kimura": "電源OFFにできませんでした。"
        }


if __name__ == '__main__':
    # set_power_on(get_physical_projector_data_from_logical_name("PJ2"))
    print(set_power_off(get_physical_projector_data_from_logical_name("PJ1")))
