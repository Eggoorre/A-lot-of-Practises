class StrandsDNA:
    '''
    class, showing dna strands

    Methods:
        __str__: returning string of dna strands
        add_strands(str): adds strand to the list of strands
        get_max_strands(str): returns strands with max len
    '''

    def __init__(self) -> None:
        '''
        initialising object of DNAs
        '''
        self.all_strands = []

    def __str__(self) -> str:
        '''
        returning dna
        :return: string of dna strands
        '''
        return ' '.join(self.all_strands)

    def add_strands(self, strands: str) -> None:
        '''
        method adding strands to the all_strands
        :param strands: strands to be added
        :return: None
        '''
        for strand in strands.strip().split():
            self.all_strands.append(strand)

    def get_max_strands(self) -> str:
        '''
        finding strands with max len
        :return: str of strands with max len else ''
        '''
        if not self.all_strands:
            return ''
        max_len = max(len(strand) for strand in self.all_strands)
        max_strands = (strand for strand in self.all_strands
                       if len(strand) == max_len)

        return ' '.join(sorted(set(max_strands)))
