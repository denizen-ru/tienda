
var category_selector;

function init_form () {
    category_selector = document.getElementById('id_category');
    category_selector.onchange = change_categories_set;
    category_selector.onkeyup = change_categories_set;
    if (category_selector.value) {
        change_categories_set();
    }
};

function change_categories_set () {
    var to_hide_list = document.getElementsByClassName('form-row');
    for (var i = 0; i < to_hide_list.length; i++) {
        var char_name = to_hide_list[i].getAttribute('class').split(' ')[1];
        if ((char_name == fixed_categories[0]) |
            (char_name == fixed_categories[1]) |
            (char_name == fixed_categories[2])) {
            continue;
        }

        to_hide_list[i].style.display = 'none';
    };

    if (category_selector.value) {
        var feature_names = categories[category_selector.value];
        for (feature in feature_names) {
            var class_name = 'field-'.concat(feature_names[feature]);
            document.getElementsByClassName(class_name)[0].style.display = 'block';
        };
    }
};
