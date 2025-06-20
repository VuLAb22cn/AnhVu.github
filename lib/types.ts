export interface Distributor {
  id: number
  name: string
  phone: string
  address: string
  region: string
  status: "Active" | "Inactive"
}
