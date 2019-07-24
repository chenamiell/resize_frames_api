class FailedToInsertTaskToCelery(Exception):
    def __init__(self):
        super().__init__('Cannot Insert Task To MQ')