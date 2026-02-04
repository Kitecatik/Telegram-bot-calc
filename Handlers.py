from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()
class Stat(StatesGroup):
    inp=State()
    

@router.message(Command('start'))
async def say_hi(message: Message, state: FSMContext):
    await state.set_state(Stat.inp)
    await message.answer(f"Привет, {message.from_user.full_name}\nВведите математическое выражение, и я дам вам ответ\nЕсли у вас будут вопросы, введите команду /help")
    
@router.message(Command('help'))
async def say_hi(message: Message):
    await message.answer("Чтобы решить ваш пример, введите команду /start\nДля отмены ввода введите команду /cancel\nВы можете применять базовые арифметические действия по типу:\n+ — сложение,\n- — вычитание,\n* — умножение,\n/ — деление,\n** — возведение в степень,\n% — узнать остаток от числа.")   

@router.message(Command('cancel'))
async def help(message: Message, state: FSMContext):
    await state.clear()

@router.message(Stat.inp) 
async def result(message: Message, state: FSMContext):
    expr = message.text
    
    if any(ch.isalpha() for ch in expr):
        await message.answer('Недопустимое выражение')
        return
    
    try:
        answer = str(eval(expr))
        await message.answer(answer)
        
    except SyntaxError:
        await message.answer('Ошибка в выражении:\nВы ввели не число.')
        
    except ZeroDivisionError:
        await message.answer('Ошибка в выражении:\nДелить на нуль нельзя.')
        
    except OverflowError:
        await message.answer('Ошибка в выражении:\nУ вас получилось огромное число с плавающей точкой.')
    
    except Exception as e:
        await message.answer(f'Ошибка в выражении:\n{e}')



