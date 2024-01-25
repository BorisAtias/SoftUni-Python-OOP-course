class Customer:
    id = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.customer_id = self.get_next_id()


    @classmethod
    def get_next_id(cls):
        next_id = Customer.id + 1
        return next_id

    def __repr__(self):
        return f"Customer <{self.customer_id}> {self.name}; Address: {self.address}; Email: {self.email}"


class Equipment:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.equipment_id = self.get_next_id()


    @classmethod
    def get_next_id(cls):
        next_id = Equipment.id + 1
        return next_id

    def __repr__(self):
        return f"Equipment <{self.equipment_id}> {self.name}"


class ExercisePlan:
    id = 1

    def __init__(self, trainer_id, equipment_id, duration):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = self.get_next_id()

    @classmethod
    def get_next_id(cls):
        next_id = ExercisePlan.id + 1
        return next_id

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        duration = hours * 60
        return cls(trainer_id, equipment_id, duration)

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"


class Subscription:
    id = 1

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.subscription_id = self.get_next_id()


    @classmethod
    def get_next_id(cls):
        next_id = Subscription.id + 1
        return next_id


def __repr__(self):
        return f"Subscription <{self.subscription_id}> on {self.date}"


class Trainer:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.trainer_id = self.get_next_id()


    @classmethod
    def get_next_id(cls):
        next_id = Trainer.id + 1
        return next_id


    def __repr__(self):
        return f"Trainer <{self.trainer_id}> {self.name}"


class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        result = ""

        subscription = [s for s in self.subscriptions if s.subscription_id == subscription_id][0]
        customer = [c for c in self.customers if c.customer_id == subscription.customer_id][0]
        trainer = [t for t in self.trainers if t.trainer_id == subscription.trainer_id][0]
        plan = [p for p in self.plans if p.exercise_plan_id == subscription.exercise_id][0]
        equipment = [e for e in self.equipment if e.equipment_id == plan.equipment_id][0]

        result += f'{subscription}\n'
        result += f'{customer}\n'
        result += f'{trainer}\n'
        result += f'{equipment}\n'
        result += f'{plan}\n'

        return result



customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))

