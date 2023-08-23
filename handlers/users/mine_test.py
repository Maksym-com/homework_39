from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states import MineStates
from keyboards.default import dynamic_reply_kb, text_button


@dp.message_handler(commands='test_mine')
async def mine(message: types.Message):
    await MineStates.State0.set()
    await message.answer("Почнімо тест по майнкрафту!")
    await message.answer("Для чого призначена дерев'яна кирка в грі?",
                        reply_markup=dynamic_reply_kb(text_button[0]))
    
@dp.message_handler(state=MineStates.State0)
async def mine0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['answer_1'] = f'{message.text}'
    await MineStates.State1.set()
    await message.answer(text="Які інгредієнти потрібно використовувати на верстаку, щоб зробити дерев'яну кирку?",
                        reply_markup=dynamic_reply_kb(text_button[1]))
    
@dp.message_handler(state=MineStates.State1)
async def mine1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['answer_2'] = f'{message.text}'
    await MineStates.State2.set()
    await message.answer("Скільки хліба у фермерів ви можете купити за 1 смарагд?",
                        reply_markup=dynamic_reply_kb(text_button[2]))

@dp.message_handler(state=MineStates.State2)
async def mine2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['answer_3'] = f'{message.text}'
    await MineStates.State3.set()
    await message.answer("Чи можна зняти сідло зі свині під час гри?",
                        reply_markup=dynamic_reply_kb(text_button[3]))
    
@dp.message_handler(state=MineStates.State3)
async def mine3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['answer_4'] = f'{message.text}'
    await MineStates.State4.set()
    await message.answer("При вбивстві свиней випадає:",
                        reply_markup=dynamic_reply_kb(text_button[4]))
    
@dp.message_handler(state=MineStates.State4)
async def mine4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['answer_5'] = f'{message.text}'
    await MineStates.State5.set()
    await message.answer("Які двері краще ставити в житло, щоб захиститися від зомбі?",
                        reply_markup=dynamic_reply_kb(text_button[5]))

@dp.message_handler(state=MineStates.State5)
async def mine5(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['answer_6'] = f'{message.text}'
    await MineStates.State6.set()
    await message.answer("Якщо гравець не спав три дня то над ним появляються:",
                        reply_markup=dynamic_reply_kb(text_button[6]))


corect_button = {
        1 : 'Для камня',
        2 : 'Палки + дошки',
        3 : '6',
        4 : 'Ні',
        5 : "1-3 куска м'яса",
        6 : 'Залізні',
        7 : 'Фантоми'
}



@dp.message_handler(state=MineStates.State6)
async def grade_mine(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['answer_7'] = f'{message.text}'
        grade = 0
        if data['answer_1'] == corect_button[1]:
            grade += 1
        if data['answer_2'] == corect_button[2]:
            grade += 1
        if data['answer_3'] == corect_button[3]:
            grade += 1
        if data['answer_4'] == corect_button[4]:
            grade += 1
        if data['answer_5'] == corect_button[5]:
            grade += 1
        if data['answer_6'] == corect_button[6]:
            grade += 1
        if data['answer_7'] == corect_button[7]:
            grade += 1
    await dp.current_state().reset_state()
    await message.answer(f"Ви пройшли тест до кінця! Ви набрали {grade}/7 балів", parse_mode='Markdown')