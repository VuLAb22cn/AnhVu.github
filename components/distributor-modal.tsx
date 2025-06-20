"use client"

import type React from "react"

import { useState, useEffect } from "react"
import type { Distributor } from "@/lib/types"

interface DistributorModalProps {
  show: boolean
  onClose: () => void
  distributor: Distributor | null
}

export function DistributorModal({ show, onClose, distributor }: DistributorModalProps) {
  const [formData, setFormData] = useState<Partial<Distributor>>({
    name: "",
    phone: "",
    address: "",
    region: "",
    status: "Active",
  })

  useEffect(() => {
    if (distributor) {
      setFormData(distributor)
    } else {
      setFormData({
        name: "",
        phone: "",
        address: "",
        region: "",
        status: "Active",
      })
    }
  }, [distributor, show])

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }))
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    // In a real application, this would call an API to save the distributor
    console.log("Form submitted:", formData)
    alert(`${distributor ? "Updated" : "Added"} distributor: ${formData.name}`)
    onClose()
  }

  return (
    <div
      className={`modal fade ${show ? "show" : ""}`}
      style={{ display: show ? "block" : "none" }}
      tabIndex={-1}
      role="dialog"
    >
      <div className="modal-dialog" role="document">
        <div className="modal-content">
          <div className="modal-header">
            <h5 className="modal-title">{distributor ? "Edit" : "Add"} Distributor</h5>
            <button type="button" className="close" onClick={onClose}>
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <form onSubmit={handleSubmit}>
            <div className="modal-body">
              <div className="form-group">
                <label htmlFor="name">Name</label>
                <input
                  type="text"
                  className="form-control"
                  id="name"
                  name="name"
                  value={formData.name}
                  onChange={handleChange}
                  required
                />
              </div>
              <div className="form-group">
                <label htmlFor="phone">Phone</label>
                <input
                  type="text"
                  className="form-control"
                  id="phone"
                  name="phone"
                  value={formData.phone}
                  onChange={handleChange}
                  required
                />
              </div>
              <div className="form-group">
                <label htmlFor="address">Address</label>
                <input
                  type="text"
                  className="form-control"
                  id="address"
                  name="address"
                  value={formData.address}
                  onChange={handleChange}
                  required
                />
              </div>
              <div className="form-group">
                <label htmlFor="region">Region</label>
                <input
                  type="text"
                  className="form-control"
                  id="region"
                  name="region"
                  value={formData.region}
                  onChange={handleChange}
                  required
                />
              </div>
              <div className="form-group">
                <label htmlFor="status">Status</label>
                <select
                  className="form-control"
                  id="status"
                  name="status"
                  value={formData.status}
                  onChange={handleChange}
                  required
                >
                  <option value="Active">Active</option>
                  <option value="Inactive">Inactive</option>
                </select>
              </div>
            </div>
            <div className="modal-footer">
              <button type="button" className="btn btn-secondary" onClick={onClose}>
                Cancel
              </button>
              <button type="submit" className="btn btn-primary">
                {distributor ? "Update" : "Add"} Distributor
              </button>
            </div>
          </form>
        </div>
      </div>
      <div className="modal-backdrop fade show"></div>
    </div>
  )
}
