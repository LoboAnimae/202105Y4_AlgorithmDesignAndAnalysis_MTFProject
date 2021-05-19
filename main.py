class MTF:
    """Move-To-First Algorithm Object"""

    def __init__(self) -> None:
        self.reset_status()
        self.load_requests()

    def reset_status(self) -> None:
        self.reset_configuration()
        self.reset_output_list()

    def load_requests(self, request_id="a", sub_request_id=1) -> None:
        if request_id == "a":
            self.requests = [j for _ in range(0, 4) for j in range(0, 5)]
        elif request_id == "b":
            self.requests = [abs(j) for _ in range(0, 2) for j in range(4, -5, -1)]
            for i, _ in enumerate(self.requests):
                try:
                    if self.requests[i - 1] == self.requests[i] and i != len(
                        self.requests
                    ):
                        self.requests.pop(i - 1)
                except:
                    pass
            self.requests.append(4)
        elif request_id == "c":
            self.requests = [0 for _ in range(0, 20)]
        elif request_id == "d":
            self.requests = [j for _ in range(0, 4) for j in range(4, -1, -1)]
        elif request_id == "e":
            content = 2 if sub_request_id == 1 else 3
            self.requests = [content for _ in range(0, 20)]

    def reset_configuration(self) -> None:
        self.configuration_list = [0, 1, 2, 3, 4]

    def reset_output_list(self) -> None:
        self.output_list = []

    def cost_perform_one(self, index):
        cost = index + 1
        conf = self.configuration_list.pop(index)
        return cost, conf

    def perform(self, index_program, function_number=1):
        for i in self.requests:
            index = self.configuration_list.index(i)
            cost, conf = (
                self.cost_perform_one(index)
                if function_number == 1
                else self.cost_perform_two(index)
            )
            self.output_list.append(cost)
            self.configuration_list[:0] = [conf]
            print(
                f"Given {i}, the cost is {cost} and the configuration remains as {self.configuration_list}"
            )

        print(
            f"Total cost for exercise {index_program} has been found to be {sum(self.output_list)}"
        )
        self.reset_status()


class IMTF:
    def __init__(self) -> None:
        self.reset_status()

    def reset_status(self) -> None:
        self.reset_configuration()
        self.reset_cost()

    def reset_configuration(self) -> None:
        self.configuration = [0, 1, 2, 3, 4]

    def reset_cost(self) -> None:
        self.cost = []

    def load_requests(self, request_id="f"):
        if request_id == "f":
            self.requests = [0 for _ in range(0, 20)]
        else:
            self.requests = [abs(j) for _ in range(0, 2) for j in range(4, -5, -1)]

    def perform(self, subindex):
        print(f"Performing {subindex} with requests {self.requests}:")
        for index, value in enumerate(self.requests):
            cost = self.configuration.index(value) + 1
            self.cost.append(cost)

            for j in range(
                index + 1,
                len(self.requests)
                if cost + index > len(self.requests)
                else (cost + index),
            ):
                if value == self.requests[j]:
                    self.configuration.insert(
                        0, self.configuration.pop(self.configuration.index(value))
                    )
            print(
                f"Given {value}, the cost is {cost} and the configuration is {self.configuration}"
            )
        print(
            f"Total cost for exercise {subindex} has been found to be {sum(self.cost)}"
        )


mtf = MTF()

options = [["a"], ["b"], ["c"], ["d"], ["ea", 1], ["eb", 2]]

for i in options:
    index = 0
    sub_index = 0
    try:
        index, sub_index = i
    except:
        index = i[0]
    print(f"For exercise {index}:")
    mtf.load_requests(index, sub_index)
    mtf.perform(index)
    print("\n\n\n")

mtf = IMTF()
mtf.load_requests()
mtf.perform("f1")

print("\n\n\n")
mtf.load_requests("z")
mtf.perform("f2")
