// var obj = { "name":"John", "age":30, "city":"New York"};
// var myJSON = JSON.stringify(obj);
// document.getElementById("demo").innerHTML = myJSON;

// var obj = ' {"name": "John", "age": "30", "city": "New York"}';
// var JSONstring = JSON.parse(obj);
// document.getElementById("demo").innertHTML = JSONstring.name + "is" + JSONstring.age;

// localStorage.setItem("Name","John");
// document.getElementById("demo").innerHTML = localStorage.getItem("obj");
/* this function gets the task from input*/
function get_todos() {
    /*This creates an array of tasks that are inputed*/
    var todos = new Array;
    /*this pulls the task that was saved in the web browser memory*/
    var todos_str = localStorage.getItem('todo1');
    /*If the input is not null the JSON.parse will communitcate
    with the web browser to make the task a JavaScript object.*/
    if (todos_str !== null); {
        todos = JSON.parse(todos_str);
    }
    return todos;
}
/*This function adds the inputed task to the get_todos function array*/
function add() {
    /*This takes the inputed task and creates a variable of it*/
    var task = document.getElementById('task').value;

    var todos = get_todos();
    /*This adds a new task the end of the array*/
    todos.push(task);
    /*this converts the task input to a JSON string*/
    localStorage.setItem('todo1', JSON.stringify(todos));
    document.getElementById("task").value = "";
    show();

    return false;
}


/*this function keeps the tasks permanently displayed on the screen*/
function show() {
    /*this sets the task that was retrieved as a variable*/
    var todos = get_todos();

    /*This sets up each task as an unordered list*/
    var html = '<ul>';
    /*This displays a task to the list in the order that it is inputed*/
    for (var i = 0; i < todos.length; i++) {
        /*this also displays the task as a list*/
        html += '<li>' + todos[i] + '<button class="remove" id="' + i + '">x</button></li>';

    };
    html += '</ul>';
    document.getElementById('todos').innerHTML = html;
}
/*This displays the inputed task when the 'Add Item' button is clicked*/
document.getElementById('add').addEventListener('click', add);
/*this will keep the inputs displayed permantaly on the screen*/
show();
