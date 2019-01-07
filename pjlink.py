from pypjlink import Projector
import settings
import os


def get_physical_projector_data_from_logical_name(logical_projector_name):
    if logical_projector_name == "PJ1":
        return {
            "result": "succeeded",
            "logical_projector_name": "{0}".format(logical_projector_name),
            "physical_projector_ip_address": os.getenv("{0}_IP_ADDRESS".format(logical_projector_name)),
            "physical_projector_password": os.getenv("{0}_PJLINK_PASSWORD".format(logical_projector_name))
        }
    elif logical_projector_name == "PJ2":
        return {
            "result": "succeeded",
            "logical_projector_name": "{0}".format(logical_projector_name),
            "physical_projector_ip_address": os.getenv("{0}_IP_ADDRESS".format(logical_projector_name)),
            "physical_projector_password": os.getenv("{0}_PJLINK_PASSWORD".format(logical_projector_name))
        }
    elif logical_projector_name == "PJ3":
        return {
            "result": "succeeded",
            "logical_projector_name": "{0}".format(logical_projector_name),
            "physical_projector_ip_address": os.getenv("{0}_IP_ADDRESS".format(logical_projector_name)),
            "physical_projector_password": os.getenv("{0}_PJLINK_PASSWORD".format(logical_projector_name))
        }
    else:
        return {
            "result": "failed",
            "message": "",
            "message_from_kimura": "プロジェクタ名は「PJ1」「PJ2」「PJ3」のどれかを指定してください。"
        }


def get_power_status(result_dict):

    projector = Projector.from_address(result_dict["physical_projector_ip_address"])
    projector.authenticate(password=result_dict["physical_projector_password"])
    return {
        "result": "succeeded",
        "logical_projector_name": result_dict["logical_projector_name"],
        "physical_projector_ip_address": result_dict["physical_projector_ip_address"],
        "projector_power_status": projector.get_power()
    }


def set_power_on(result_dict):
    projector = Projector.from_address(result_dict["physical_projector_ip_address"])
    projector.authenticate(password=result_dict["physical_projector_password"])

    if projector.get_power() == "off":
        projector.set_power("on")
        return {
            "result": "succeeded",
            "logical_projector_name": result_dict["logical_projector_name"],
            "physical_projector_ip_address": result_dict["physical_projector_ip_address"],
            "projector_power_status": projector.get_power()
        }
    else:
        return {
            "result": "succeeded",
            "message_from_kimura": "プロジェクターはすでに電源ONか、起動前・終了後の状態です。",
            "logical_projector_name": result_dict["logical_projector_name"],
            "physical_projector_ip_address": result_dict["physical_projector_ip_address"],
            "projector_power_status": projector.get_power()
        }


def set_power_off(result_dict):
    projector = Projector.from_address(result_dict["physical_projector_ip_address"])
    projector.authenticate(password=result_dict["physical_projector_password"])

    if projector.get_power() == "on":
        projector.set_power("off")
        return {
            "result": "succeeded",
            "logical_projector_name": result_dict["logical_projector_name"],
            "physical_projector_ip_address": result_dict["physical_projector_ip_address"],
            "projector_power_status": projector.get_power()
        }
    elif projector.get_power() == "cooling":
        return {
            "result": "succeeded",
            "message_from_kimura": "プロジェクターは終了後の冷却状態です。",
            "logical_projector_name": result_dict["logical_projector_name"],
            "physical_projector_ip_address": result_dict["physical_projector_ip_address"],
            "projector_power_status": projector.get_power()
        }
    elif projector.get_power() == "warm-up":
        return {
            "result": "succeeded",
            "message_from_kimura": "プロジェクターは起動前のウォーミングアップ状態です。",
            "logical_projector_name": result_dict["logical_projector_name"],
            "physical_projector_ip_address": result_dict["physical_projector_ip_address"],
            "projector_power_status": projector.get_power()
        }
    else:
        return {
            "result": "succeeded",
            "message_from_kimura": "プロジェクターはすでに電源OFFの状態です。",
            "logical_projector_name": result_dict["logical_projector_name"],
            "physical_projector_ip_address": result_dict["physical_projector_ip_address"],
            "projector_power_status": projector.get_power()
        }


if __name__ == '__main__':
    print(get_power_status(get_physical_projector_data_from_logical_name("PJ2")))
    # print(set_power_on(get_physical_projector_data_from_logical_name("PJ2")))
    print(set_power_off(get_physical_projector_data_from_logical_name("PJ2")))
