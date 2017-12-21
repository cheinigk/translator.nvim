class EitherMonad(object):

    """Holds one of two things."""

    def __init__(self, left, right, is_left_active):
        """Initializes the EitherMonad with a thing.

        :left: First thing.
        :right: Second thing.
        :is_left_active: Whether EitherMonad holds left or not.

        """
        self._left = left
        self._right = right
        self._is_left_active = is_left_active

    def map(self, lfun, rfun):
        """Applies lfun to left or rfun to right.

        :lfun: A function that receives a left.
        :rfun: A function that receives a right.
        :returns: An EitherMonad.

        """
        return self.lmap(lfun).rmap(rfun)
        
    def lmap(self, fun):
        """Applies a function to the left thing or does nothing.

        :fun: The function that shall be evaluated.
        :returns: An EitherMonad.

        """
        if is_left_active:
            return EitherMonad(fun(self._left), self._right, True)
        else:
            return self
        
    def rmap(self, fun):
        """Applies a function to the right thing or does nothing.

        :fun: The function that shall be evaluated.
        :returns: An EitherMonad.

        """
        if not is_left_active:
            return EitherMonad(self._left, fun(self._right), False)
        else:
            return self
