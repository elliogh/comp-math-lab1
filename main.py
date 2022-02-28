from input import get_matrix
from solve import do_gauss_method, do_residual_vector

try:
    main_matrix = get_matrix()
    answer_matrix = do_gauss_method(main_matrix)
    do_residual_vector(main_matrix, answer_matrix)
except Exception as ex:
    template = "Что-то пошло не так!...\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)