# python-flows

Create a git repository to host your source code. Git repository has source code folder to execution python code

commands to execute
1. Create a pipeline resource
```
kubectl apply -f flows/00-math-pipeline-resource.yml  # edit url in this folder to match your repository
```
2. Create a task to add two numbers (no validation check in the code assuming right values are passed)
```
kubectl apply -f flows/01-task-add.yml
```
3. To run math-add task
```
tkn task start math-add
```
To check the output of the task run follow the instructions on the command prompt
4. To create task run for math-add
```
tkn task start math-add --dry-run
```
5. To create a new task run using kubectl command store the ouput of step 4 into a file.  In my case the output is stored into flows/06-taskRun-add.yml
```
kubectl create -f flows/06-taskRun-add.yml
```
To check logs of kubectl command
```
tkn taskrun logs --last -f
```
6. Created addtional task/taskrun for substraction, multiplication and division using step 2, 4 & 5
    * flows/02-task-subtract.yml
    * flows/03-task-multiply.yml
    * flows/04-task-divide.yml
    * flows/06-taskRun-subtract.yml
    * flows/07-taskRun-multiply.yml
    * flows/08-taskRun-divide.yml
7. Now it is time to orchestrate this functions in sequential order, refer to flows/10-pipeline-math-seq.yml
```
kubectl apply -f flows/10-pipeline-math-seq.yml
```
8. To create a pipeline run
```
tkn pipeline start math-sequential
```
9. To create pipeline run
```
tkn pipeline start math-sequential --dry-run
```
10. To create a kubectl run using kubectl command store the ouput of step 9 into a file.  In my case the output is stored into flows/10-pipeline-math-seq.yml
```
kubectl create -f flows/10-pipeline-math-seq.yml
tkn pipelinerun logs --last -f
```
11. To create pipeline for parallel run
```
kubectl apply -f flow/12-pipepline-math-paralle.yml
tkn pipeline start math-parallel --dry-run
# Copy contents of the output to flows/13-pipelineRun-math-parallel.yml
kubectl create -f flows/13-pipelineRun-math-parallel.yml
tkn pipelinerun logs --last -f
```
12. Next up passing parametets to tasks.  Parameters type supported are string & array.  To pass an array use comma separated values (no spaces between comma and value) \
    In flows/14-task-add-params.yml I am passing parameters as string variables and for flows/16-task-subtract-params.yml values are passed as an array.  \
    This made things interesting in pipeline, follow parameter pl-param-xy in flows/18-pipeline-math-seq-params.yml
```
kubectl apply -f flows/14-task-add-params.yml
tkn task start math-add-params --dry-run
# output of above command is copied to flows/15-taskRun-add-params.yml
kubectl create -f flows/15-taskRun-add-params.yml
tkn taskrun logs --last -f
kubectl apply -f flows/16-task-subtract-params.yml
tkn task start math-subtract-params --dry-run
kubectl create -f flows/17-taskRun-subtract-params.yml
tkn taskrun logs --last -f
```
13. Creating a pipeline for params to execute in sequence, as mentioned above passing array parameters made things interesting
```
kubectl apply -f flows/18-pipeline-math-seq-params.yml
tkn pipeline start math-sequential-params --dry-run
# Copy output to flows/19-pipelineRun-math-seq-params.yml
kubectl create -f flows/19-pipelineRun-math-seq-params.yml
tkn pipelinerun logs --last -f
```

99. To run things on minikube
```
kubectl apply --filename https://storage.googleapis.com/tekton-releases/pipeline/latest/release.yaml
kubectl apply --filename https://github.com/tektoncd/dashboard/releases/latest/download/tekton-dashboard-release.yaml
# to switch to tekton-pipelines namespace
kubectl config set-context --current --namespace=tekton-pipelines
kubectl proxy --port=8080
# Dash board can now be accessed at http://localhost:8080
```