def validate_results(students, pass_mark, max_mark, grace_pool):
    results = {}
    for name in students:
        marks = students[name]
        updated_marks = {}
        pool_left = grace_pool
        failed_count = 0
        
        
        for sub in marks:
            score = marks[sub]
            if score < pass_mark:
                needed = pass_mark - score
                if pool_left >= needed:
                    pool_left -= needed
                    score = pass_mark  
            
            
            if score > max_mark:
                score = max_mark
                
            if score < pass_mark:
                failed_count += 1
                
            updated_marks[sub] = score
            
        
        if failed_count == 0:
            status = "Pass"
        else:
            status = "Fail (" + str(failed_count) + " subjects)"
            
        results[name] = {"marks": updated_marks, "status": status}
    return results


student_data = {
    "John": {"Math": 32, "Science": 45, "History": 78},  
    "Mary": {"Math": 28, "Science": 30, "History": 85}   
}

print("11:", validate_results(student_data, pass_mark=35, max_mark=100, grace_pool=5))
