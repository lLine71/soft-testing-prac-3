
from behave import given, when, then
from game import Game

@given('Игра началась')
def step_give_game_started(context):
    context.game = Game()

@when('я ввожу "{chrs}"')
def step_when_enter_str(context, chrs):
    context.result = context.game.play(chrs)

@then('результат должен быть "{expected_result}"')
def step_then_verify_result(context, expected_result):
    assert context.result == expected_result, f'Ожидался результат'


