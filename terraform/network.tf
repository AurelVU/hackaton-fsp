resource "yandex_vpc_network" "hackaton" {
  name = "hackaton"
  folder_id = "${yandex_resourcemanager_folder.hackaton.id}"
}

resource "yandex_vpc_subnet" "hackaton-cluster" {
  name = "hackaton-cluster"
  zone = "ru-central1-b"
  network_id = yandex_vpc_network.hackaton.id
  v4_cidr_blocks = ["10.11.0.0/16"]
  folder_id = "${yandex_resourcemanager_folder.hackaton.id}"
}