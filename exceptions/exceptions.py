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


class TryingToAddExistingColor(CustomLogicException):
    def __init__(self, message='It is impossible to add color which already exists'):
        super().__init__(message)


class TryingToLoadNonexistingSaving(CustomLogicException):
    def __init__(self, message='It is impossible to load saving which doesnt exist'):
        super().__init__(message)


class TryingToDeleteNonexistingSaving(CustomLogicException):
    def __init__(self, message='It is impossible to delete saving which doesnt exist'):
        super().__init__(message)


class TryingToDeleteNonSavedGraph(CustomLogicException):
    def __init__(self, message='It is impossible to delete all savings of graph which was not saved'):
        super().__init__(message)


class TryingToDeleteNonLoadedGraph(CustomLogicException):
    def __init__(self, message='It is impossible to delete graph which is not loaded'):
        super().__init__(message)


class NoGraphLoadedToDelete(CustomLogicException):
    def __int__(self, message='You cant delete current graph due to no graph is loaded'):
        super().__int__(message)


class TryingToLoadNonexistingGraph(CustomLogicException):
    def __int__(self, message='You cant load graph which does not exist'):
        super().__int__(message)


class TryingToAddEdgeBetweenGraphs(CustomLogicException):
    def __int__(self, message='You can not add edge inbetween two different graphs'):
        super().__int__(message)