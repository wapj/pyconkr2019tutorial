# django 코드의 일부분입니다.
class ModelBase(type):
    """
    Metaclass for all models.
    """

    def __new__(cls, name, bases, attrs):
        super_new = super().__new__

        app_label = None

        if getattr(meta, "app_label", None) is None:
            raise RuntimeError(
                "Model class %s.%s doesn't declare an explicit "
                "app_label and isn't in an application in "
                "INSTALLED_APPS." % (module, name)
            )
