from logzero import logger as log
from db_connection import DataBaseObj
from app_models import MobileInfo

db_obj = DataBaseObj()


class MobileInfoDB(object):
    @staticmethod
    def query_mobile_info(mobile_id):
        log.debug(f"query_mobile_info {mobile_id}")
        session = db_obj.get_db_session()
        try:
            query_result = session.query(MobileInfo)
            if mobile_id == "-1":
                result = query_result.all()
            else:
                result = query_result.filter(MobileInfo.mobile_id == mobile_id).all()
            session.commit()
            log.debug(result)
        except Exception as e:
            session.rollback
            log.exception(f"query_mobile_info failed {str(e)}")
        finally:
            session.close()
            log.debug(f"session closed")
        return result

    @staticmethod
    def add_mobile_info(mobile_info):
        log.debug(f"add_mobile_info {mobile_info}")
        session = db_obj.get_db_session()
        try:
            count_result = (
                session.query(MobileInfo)
                .filter(MobileInfo.mobile_id == mobile_info.mobile_id)
                .count()
            )
            if count_result > 0:
                log.error(f"mobile already exists {mobile_info.mobile_id}")
            else:
                new_mobile = MobileInfo(
                    mobile_id=mobile_info.mobile_id,
                    mobile_name=mobile_info.mobile_name,
                    brand_id=mobile_info.brand_id,
                    storage_size=mobile_info.storage_size,
                    ram_size=mobile_info.ram_size,
                )

                log.debug(f"add_mobile_info {new_mobile}")
                session.add(new_mobile)
                session.commit()
        except Exception as e:
            session.rollback
            log.exception(f"add_mobile_info failed {str(e)}")
        finally:
            session.close()
            log.debug(f"session closed")

    @staticmethod
    def update_mobile_info(mobile_id, mobile_info):
        log.debug(f"update_mobile_info {mobile_info}")
        session = db_obj.get_db_session()
        try:
            query_result = session.query(MobileInfo).filter(
                MobileInfo.mobile_id == mobile_id
            )
            if query_result.count() == 0:
                log.error(f" mobile not found", mobile_info.mobile_id)
            else:
                query_result.update(
                    {
                        MobileInfo.mobile_name: mobile_info.mobile_name,
                        MobileInfo.brand_id: mobile_info.brand_id,
                        MobileInfo.storage_size: mobile_info.storage_size,
                        MobileInfo.ram_size: mobile_info.ram_size,
                    }
                )

                session.commit()
                result = MobileInfo
        except Exception as e:
            session.rollback
            log.exception(f"update_mobile_info failed {str(e)}")
        finally:
            session.close()
            log.debug(f"session closed")
        return result

    @staticmethod
    def delete_mobile_info(mobile_id):
        log.debug(f"delete_mobile_info {mobile_id}")
        session = db_obj.get_db_session()
        try:
            query_result = session.query(MobileInfo).filter(
                MobileInfo.mobile_id == mobile_id
            )
            if query_result.count() == 0:
                log.error(f" mobile not found {mobile_id}")
                result = 0
            else:
                result = query_result.delete()
            session.commit()
        except Exception as e:
            session.rollback
            log.exception(f"delete_mobile_info failed {str(e)}")
        finally:
                session.close()
                log.debug(f"session closed")
        return result

    