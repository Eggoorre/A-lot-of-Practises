class TrafficLight:
    '''
    class representing traffic light
    Attributes:
        current_signal(str): showing current signal on a traffic light
        signal_before(str): showing signal before

    Methods:
        next_signal(): changing colour of tge traffic light
    '''
    def __init__(self) -> None:
        '''
        initialising traffic light
        '''
        self.colours = ['Зелёный', 'Жёлтый', 'Красный']
        self.current_signal = self.colours[0]
        self.signal_before = None

    def next_signal(self) -> None:
        '''
        method changing colour of the traffic light
        :return: None
        '''
        if self.current_signal == self.colours[0]:
            self.current_signal = self.colours[1]
            self.signal_before = self.colours[0]

        elif self.current_signal == self.colours[2]:
            self.current_signal = self.colours[1]
            self.signal_before = self.colours[2]

        elif (self.current_signal == self.colours[1]
              and self.signal_before == self.colours[0]):
            self.current_signal = self.colours[2]

        elif (self.current_signal == self.colours[1]
              and self.signal_before == self.colours[2]):
            self.current_signal = self.colours[0]
