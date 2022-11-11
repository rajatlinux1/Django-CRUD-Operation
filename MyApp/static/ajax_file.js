console.log("Ajax tutorial in one video");


let Update_Btn = document.getElementById('data_update');
Update_Btn.addEventListener('click', buttonClickHandler)

function buttonClickHandler() {
     console.log('You have clicked the Update Button');
     var name=$("input[name=Name]").val()
     var age=$("input[name=Age]").val()
     var contact=$("input[name=Contact]").val()

     console.log(name)
     console.log(age)
     console.log(contact)
}
 //   // Instantiate an xhr object
 //   const xhr = new XMLHttpRequest();
//
 //   // Open the object
 //   // xhr.open('GET', 'https://jsonplaceholder.typicode.com/todos/1', true);
//
 //   // USE THIS FOR POST REQUEST
 //   xhr.open('POST', 'http://dummy.restapiexample.com/api/v1/create', true);
 //   xhr.getResponseHeader('Content-type', 'application/json');
//
//
 //   // What to do on progress (optional)
 //   xhr.onprogress = function(){
 //       console.log('On progress');
 //   }
//
//
 //   // xhr.onreadystatechange = function () {
 //   //     console.log('ready state is ', xhr.readyState);
 //       
 //   // }
//
 //   // What to do when response is ready
 //   xhr.onload = function () {
 //       if(this.status === 200){
//
 //           console.log(this.responseText)
 //       }
 //       else{
 //           console.log("Some error occured")
 //       }
 //   }
//
 //   // send the request
 //   params = `{"name":"test34sad545","salary":"123","age":"23"}`;
 //   xhr.send(params);
//
 //   console.log("We are done!");
//
//}//xhr.onprogress = function(){
 //       console.log('On progress');
 //   }
//
//
 //   // xhr.onreadystatechange = function () {
 //   //     console.log('ready state is ', xhr.readyState);
 //       
 //   // }
//
 //   // What to do when response is ready
 //   xhr.onload = function () {
 //       if(this.status === 200){
//
 //           console.log(this.responseText)
 //       }
 //       else{
 //           console.log("Some error occured")
 //       }
 //   }
//
 //   // send the request
 //   params = `{"name":"test34sad545","salary":"123","age":"23"}`;
 //   xhr.send(params);
//
 //   console.log("We are done!");