"use client"

import { useState } from "react"
import type { Distributor } from "@/lib/types"
import { distributors } from "@/lib/data"

interface DistributorTableProps {
  onEdit: (distributor: Distributor) => void
}

export function DistributorTable({ onEdit }: DistributorTableProps) {
  const [data] = useState<Distributor[]>(distributors)

  const handleDelete = (id: number) => {
    // In a real application, this would call an API to delete the distributor
    alert(`Delete distributor with ID: ${id}`)
  }

  return (
    <div className="table-responsive">
      <table className="table table-striped table-hover">
        <thead className="thead-light">
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Phone</th>
            <th>Address</th>
            <th>Region</th>
            <th>Status</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {data.map((distributor) => (
            <tr key={distributor.id}>
              <td>{distributor.id}</td>
              <td>{distributor.name}</td>
              <td>{distributor.phone}</td>
              <td>{distributor.address}</td>
              <td>{distributor.region}</td>
              <td>
                <span className={`badge badge-${distributor.status === "Active" ? "success" : "danger"}`}>
                  {distributor.status}
                </span>
              </td>
              <td>
                <button className="btn btn-sm btn-primary mr-1" onClick={() => onEdit(distributor)}>
                  Edit
                </button>
                <button className="btn btn-sm btn-danger" onClick={() => handleDelete(distributor.id)}>
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
