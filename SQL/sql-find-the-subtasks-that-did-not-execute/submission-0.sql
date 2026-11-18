-- Write your query below
with recursive r_subtasks as
(

    select 1 as subtask
    union all
    select subtask+1 from r_subtasks
    where subtask<(select max(subtasks_count) from tasks)
)
,task_final as
(

    select task_id,subtask as subtask_id
    from tasks t join r_subtasks r on t.subtasks_count>=r.subtask
)
select t.task_id,t.subtask_id
from task_final t left join executed e
on t.task_id=e.task_id and t.subtask_id=e.subtask_id
where e.task_id is NULL