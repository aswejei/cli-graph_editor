class CustomLogicException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class TryingToAddExistingNodeException(CustomLogicException):
    def __init__(self, message='You can not add a node that already exists'):
        super().__init__(message)


class TryingToDeleteUnexistingEdgeException(CustomLogicException):
    def __init__(self, message='It is impossible to delete edge which does not exist'):
        super().__init__(message)


class TryingToDeleteUnexistingNodeException(CustomLogicException):
    def __init__(self, message='It is impossible to delete node which does not exist'):
        super().__init__(message)


class TryingToSetNameForUnexistingNode(CustomLogicException):
    def __init__(self, message='It is impossible to set name for node which does not exist'):
        super().__init__(message)

class TryingToAddEdgeWhichDoesntMatchGraphOrientation(CustomLogicException):
    def __init__(self, message='It is impossible to add edge to graph if their orientation does not match'):
        super().__init__(message)
