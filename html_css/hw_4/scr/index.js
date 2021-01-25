let letters = [];
let letters2 = "Backend As A Service";
let letters3 = letters2.split(' ');

for (let i = 0; i != letters3.length;i++){
	letters.push(letters3[i][0])
}
console.log(letters)
console.log(letters.join(''))


function hw2(date) {
  if (typeof date === "number") {
    console.log(new Date().toLocaleString())
  } else {
    console.log('Неверный тип данных')
  }
}
hw2(24)


function hw3(){

	console.log(arguments)

}
console.log(hw3(10, false, "google"))

//hw4
function userInfo(people){
	if (people.registered == true) {
		console.log('Дата регистрации: ' + people.data)
	}
	if (people.registered == false){
		console.log('Незарегистрированный пользователь: ' + people.name)
	}
	
}



let people = {
	name :'John Doe',
	registered : true,
	data : '24.01.2020',
	
}

let people2 = {
	name : 'John Doe2',
	registered : false,
	data : '23.01.2020',
	
}

userInfo(people)
userInfo(people2)

//hw5
// you should write the code of function  getCurrentPostComments

var users = {
        14587: {
                name: "Ivan",
                email: "ivan78@gmail.com"
        },
        28419: {
                name: "Georg",
                email: "georg.klep@gmail.com"
        },
        41457: {
                name: "Stephan",
                email: "stephan.borg@gmail.com"
        }
}
var posts = {
        7891451: {
                author: 14587,
                text: "Imagine we can encapsulate these secondary responsibilities in functions"
        },
        7891452: {
                author: 28419,
                text: `В конструкторе ключевое слово super используется как функция, вызывающая родительский конструктор. 
                        Её необходимо вызвать до первого обращения к ключевому слову this в теле конструктора. 
                        Ключевое слово super также может быть использовано для вызова функций родительского объекта`
        },
        7891453: {
                author: 28419,
                text: `DOM не обрабатывает или не вынуждает проверять пространство имен как таковое. 
                        Префикс пространства имен, когда он связан с конкретным узлом, не может быть изменен`
        },
        7891454: {
                author: 14587,
                text: "Ключевое слово super используется для вызова функций, принадлежащих родителю объекта"
        }
}
var comments = {
        91078454: {
                postId: 7891451,
                author: 28419,
                text: `The static String.fromCharCode() method returns a string created 
                        from the specified sequence of UTF-16 code units`
        },
        91078455: {
                postId: 7891451,
                author: 41457,
                text: `HTML элемент <template> — это механизм для отложенного рендера клиентского контента, 
                        который не отображается во время загрузки, но может быть инициализирован при помощи JavaScript`
        },
        91078457: {
                postId: 7891452,
                author: 41457,
                text: "Глобальный объект String является конструктором строк, или, последовательностей символов"
        },
        91078458: {
                postId: 7891452,
                author: 14587,
                text: `The Element.namespaceURI read-only property returns the namespace URI of the element, 
                        or null if the element is not in a namespace`
        }
}

function getCurrentPostComments ( postId ) {
        var res = []
        for(let i in comments){
        	commentarie = comments[i];
        	commentAuthor = users[commentarie.author];
        	userName = commentAuthor.name;
        	if(postId == commentarie.postId){
        		res.push({
        			author: userName,
        			text: commentarie.text
        		})
        	}
        }
        return res
}

console.log(getCurrentPostComments(7891451))