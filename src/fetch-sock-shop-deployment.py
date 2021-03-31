# get deployment by namespace
from kubernetes import client, config
config.load_kube_config()
apis_api = client.AppsV1Api()
print("Listing pods of namespace:")
resp = apis_api.list_namespaced_deployment(namespace="sock-shop")
print("Details of sock-shop deployment")
print("Name of Deployment\t\tImage\t\tDate of Update")
for i in resp.items:
    print("%s\t\t%s\t\t%s" % (i.metadata.name,i.spec.template.spec.containers[0].image,i.status.conditions[0].last_update_time))