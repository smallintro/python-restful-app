from logzero import logger as log
from db_operation import MobileInfoDB

mobile_db = MobileInfoDB()


class MobileInfoService(object):
    @staticmethod
    def get_mobile_info(mobile_id):
        log.debug(f"get_mobile_info")
        result = mobile_db.query_mobile_info(mobile_id)
        return result

    @staticmethod
    def add_mobile_info(mobile_info):
        log.debug(f"add_mobile_info")
        mobile_db.add_mobile_info(mobile_info)
        result = mobile_db.query_mobile_info(mobile_info.mobile_id)
        return result

    @staticmethod
    def update_mobile_info(mobile_id, mobile_info):
        log.debug(f"update_mobile_info")
        result = mobile_db.update_mobile_info(mobile_id, mobile_info)
        return result

    @staticmethod
    def del_mobile_info(mobile_id):
        log.debug(f"del_mobile_info")
        result = mobile_db.delete_mobile_info(mobile_id)
        return result
