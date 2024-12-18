-- 코드를 작성해주세요
with fish as (
    select id, length
    from fish_info
    order by length desc, id 
)
select id, length
from fish
limit 10
