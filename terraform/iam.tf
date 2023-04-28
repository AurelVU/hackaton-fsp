resource "yandex_iam_service_account" "hackaton" {
  name        = "hackaton-editor"
  description = "service account to manage hackaton infra"
  folder_id = "${yandex_resourcemanager_folder.hackaton.id}"
}

resource "yandex_resourcemanager_folder" "hackaton" {
    name = "hackaton"
}

resource "yandex_resourcemanager_folder_iam_member" "hackaton" {
  folder_id = "${yandex_resourcemanager_folder.hackaton.id}"
  role      = "editor"
  member    = "serviceAccount:${yandex_iam_service_account.hackaton.id}"
}