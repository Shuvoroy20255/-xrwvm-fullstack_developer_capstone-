def show_exam_result(request, course_id, submission_id):
    context = {}
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    questions = submission.enrollment.course.question_set.all()
    total_score = 0
    selected_ids = []
    possible_score = 0

    for question in questions:
        possible_score += question.is_get_score(submission.choices.all())
        selected_choice = submission.choices.filter(question=question).first()
        if selected_choice:
            selected_ids.append(selected_choice.id)
            if selected_choice.is_correct:
                total_score += 1

    context['course'] = course
    context['submission'] = submission
    context['questions'] = questions
    context['selected_ids'] = selected_ids
    context['possible_score'] = possible_score
    context['total_score'] = total_score

    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
