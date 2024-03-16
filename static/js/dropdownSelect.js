function dropdownSelect() {
    $('select').each(function (i, select) {
        // console.log(i)
        // console.log(select)
        // var a = '';
        // var b = 'b';
        // console.log(a || b); //(a!=null) ? a : b
        $(this).after('<div class="dropdown-select ' + ($(this).attr('class') || '') + ' " tabindex="0">' +
            '<span class="dropdown-select__current"></span>' +
            '<div class="dropdown-select__list">' +
            '<ul class="dropdown-select__ul"></ul>' +
            '</div>' +
            '</div>');

        var dropdown = $(this).next();
        var options = $(select).find('option');
        var selected = $(this).find('option:selected');
        dropdown.find('.dropdown-select__current').html(selected.text());

        options.each(function (j, o) {
            var dropdown__option = '<li class="dropdown-select__option  ' + ($(o).is(':selected') ? 'dropdown-select--selected' : '') + ' " data-value="' + $(o).val() + '" tabindex="0">' + $(o).text() + '</li>';
            dropdown.find('ul').append(dropdown__option);
        })
    })
    $(document).on('click', '.dropdown-select', function () {
        $('.dropdown-select').not($(this)).removeClass('dropdown-select--open');
        $(this).toggleClass('dropdown-select--open');
        if ($(this).hasClass('dropdown-select--open')) {
            $(this).find('.dropdown-select__option').attr('tabIndex', 0);
            $(this).find('dropdown-select--selected').focus();
        } else {
            $(this).find('.dropdown-select__option').removeAttr('tabIndex');
            $(this).focus();
        }
    })
    $(document).on('click', function (e) {
        if ($(e.target).closest('.dropdown-select').length === 0) {
            $('.dropdown-select').removeClass('dropdown-select--open');
            $('.dropdown-select__option').removeAttr('tabIndex');
        }
    })


    $(document).on('click', '.dropdown-select__option', function () {
        // console.log($(this));
        $(this).closest('.dropdown-select__list').find('.dropdown-select--selected').removeClass('dropdown-select--selected');
        $(this).addClass('dropdown-select--selected');
        var text = $(this).text();
        $(this).closest('.dropdown-select').find('.dropdown-select__current').text(text);
        var data__value = $(this).data('value')
        $(this).closest('.dropdown-select').prev('select').val(data__value).trigger('change');
        console.log($(this).closest('.dropdown-select').prev('select'));

    })

}

dropdownSelect();