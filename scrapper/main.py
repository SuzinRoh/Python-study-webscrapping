from indeed import get_jobs as get_indeed_jobs
from incruit import get_jobs as get_inc_jobs
from save import save_to_file

indeed_jobs = get_indeed_jobs()
inc_jobs = get_inc_jobs()

jobs = indeed_jobs + inc_jobs

save_to_file(jobs)

