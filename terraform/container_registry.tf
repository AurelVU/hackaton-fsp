resource "yandex_container_registry" "hackaton" {
  name = "hackaton"
  folder_id = "${yandex_resourcemanager_folder.hackaton.id}"
}