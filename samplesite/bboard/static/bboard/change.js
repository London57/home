

// const editBtn = document.getElementById('editBtn');
// const profile = document.getElementById('profile_before');
// const editModal = document.getElementById('editModal');
// const editFLname = document.getElementById('FLfirst');
// const FLname = document.getElementById('editFLname');
// const editDayBorn = document.getElementById('birth_date');
// const DayBorn = document.getElementById('editDayBorn');
// const editPhone = document.getElementById('phone_number');
// const phone = document.getElementById('editPhone');
// const editForm = document.getElementById('editForm');
const test = document.getElementById('test');

// // Обработчик нажатия на кнопку "Изменить"
// editBtn.addEventListener('click', function() {
//     // Заполнение формы текущими данными пользователя
//     FLname.value = editFLname.innerText;
//     DayBorn.value = editDayBorn.innerText;
//     phone.value = editPhone.innerText;

//     // Отображение модального окна
//     profile.style.display = 'none';
//     editModal.style.display = 'block';
// });

// // Обработчик отправки формы редактирования
// editForm.addEventListener('submit', function(event) {
//     event.preventDefault();
//     editModal.style.display = 'none';
//     profile.style.display = 'block';
//     // Обновление данных пользователя с данными из формы
//     editFLname.innerText = FLname.value;
//     editDayBorn.innerText = DayBorn.value;
//     editPhone.innerText = phone.value;
//     const formData = new FormData(editForm);

//     fetch('/test_fetch/', {
//       method: 'POST',
//       body: 'bb'
//     })
//       .then(response => response.json())
//       .then(data => {
//         console.log(data.message); // Печатает сообщение из JsonResponse
  
//         // Очистка полей формы
//        editForm.reset();
//       })
//       .catch(error => {
//         console.error('Произошла ошибка:', error);
//       });
  
//     // Закрытие модального окна

//     // Очистка полей формы
    
// });


test.addEventListener('onclick', function(){
    fetch('test_fetch', {
        method: 'POST',
        body: 'bb'
    })
})
