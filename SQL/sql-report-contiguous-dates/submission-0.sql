-- Write your query below
with combined as
(
select success_date as event_date, 'succeeded' as state
from succeeded
where success_date between '2019-01-01' and '2019-12-31'
union all
select fail_date , 'failed' 
from failed
where fail_date between '2019-01-01' and '2019-12-31'
order by 1
)
,lag_flag as
(
    select case when COALESCE(lag(state) over(order by event_date),state) !=state then 1 else 0 end as flag,
    state,
    event_date 
    from combined
)
,rolling_sum as
(

    select sum(flag) over(order by event_date) as island,
    state,event_date
    from lag_flag
)
select 
state as period_state
,min(event_date) as start_date
,max(event_date) as end_date

from rolling_sum
group by state,island
order by 2