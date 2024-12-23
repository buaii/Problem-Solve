-- 코드를 작성해주세요
select count(*) as fish_count, fish_name
from fish_info
join fish_name_info
on fish_info.fish_type = fish_name_info.fish_type
group by fish_info.fish_type, fish_name
order by fish_count desc