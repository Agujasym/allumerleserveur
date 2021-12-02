STORAGE_KEY=$(az storage account keys list \
--resource-group minecraft \
--account-name jabasminecraft \
--query "[0].value" \
--output tsv)

az container create \
--resource-group minecraft \
--name minecraftcontainer \
--cpu 1 \
--memory 8 \
--image itzg/minecraft-server \
--dns-name-label cestnotreprojet \
--ports 25565 \
--azure-file-volume-account-name jabasminecraft \
--azure-file-volume-account-key $STORAGE_KEY \
--azure-file-volume-share-name minecraft \
--azure-file-volume-mount-path /data \
--environment-variables EULA=TRUE OPS=AgujaSym MEMORY=6G