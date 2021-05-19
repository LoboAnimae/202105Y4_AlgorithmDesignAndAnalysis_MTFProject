configuration_list = [0, 1, 2, 3, 4]


class MTFObject:
    def __init__(self) -> None:
        self.configuration_list = [0, 1, 2, 3, 4]
        self.output_list = []
        self.load_requests()

    def load_requests(self, request_id=1) -> None:
        if request_id == 1:
            self.requests = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
        elif request_id == 2:
            self.requests = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]
