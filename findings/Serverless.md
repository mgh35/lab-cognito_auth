# Some notes on Serverless

## Output

Serverless allows specifying `output` at the top level of the `serverless.yml` file. These get sent to the Serverless 
Pro account (and then displayed on the Dashboard or retrieved with `sls output`).

But for AWS, at least, CloudFormation lets you define Output resources (which are defined under `resources.Outputs`). 
You can see them with `sls info -v` as 'Stack Outputs'. This plugin captures them to a file: 
[serverless-stack-output](https://github.com/sbstjn/serverless-stack-output)


## References

https://lorenstewart.me/2017/09/19/serverless-framework-terminal-commands/

https://github.com/sbstjn/serverless-stack-output