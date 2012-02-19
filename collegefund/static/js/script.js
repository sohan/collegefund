$(document).ready(function() { 

    //start the carousel
    //$('.carousel').carousel();

    //bind to hover and click
    $('.student_in_table').live('mouseover', get_student_in_spotlight);
    $('.student_in_table').live('click', get_student_in_spotlight);

    //set student spotlight initially 
    show_student_in_spotlight(students[0]);

    //student spotlight
    var table_rows = 3;
    var table_cols = 3;
    var table = $('#select_student_spotlight');
    for (var i = 0; i < table_rows; i++) {
        var row = $('<tr></tr>');
        table.append(row);
        for (var j = 0; j < table_cols; j++) {
            var index = i*table_rows + j;
            var cell = $('<td id="student' + index +'" class="student_in_table"></td>');
            row.append(cell);
            var picture = $('<a href="#" class="thumbnail"></a>'); 
            cell.append(picture);
            var pic_src = $('<img src="' +
                    'http://placehold.it/160x120' +
                    '"></img>');
            if ((index) < students.length) {
                var student = students[i*table_rows + j];
                if (student['photo']) {
                    pic_src =$('<img src="' + student['photo'] +
                        '"></img>');
                }
            }
            picture.append(pic_src);
        }
    }
});

var get_student_in_spotlight = function() {
    console.log('get student in spotlight');
    var index = $(this).attr('id').replace('student', '');
    index = +index;
    var student = students[index];
    show_student_in_spotlight(student);
}

var show_student_in_spotlight = function(student) {
    var spotlight = $('#student_in_spotlight');
    spotlight.empty();
    if (student) {
        spotlight.append($('<h5>' + student['name'] + '</h5>'));
        spotlight.append($('<p>' + student['university'] + '</p>'));
    }
}
