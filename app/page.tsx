"use client"

import { useState } from "react"

export default function Dashboard() {
  const [showModal, setShowModal] = useState(false)

  const handleOpenModal = () => setShowModal(true)
  const handleCloseModal = () => setShowModal(false)

  return (
    <div className="wrapper">
      {/* Top Navbar */}
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
        <a className="navbar-brand" href="#">
          <img src="/placeholder.svg?height=30&width=120" alt="Logo" height="30" />
        </a>
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent">
          <span className="navbar-toggler-icon"></span>
        </button>

        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav ml-auto">
            <li className="nav-item dropdown">
              <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown">
                <img
                  src="/placeholder.svg?height=30&width=30"
                  className="rounded-circle mr-2"
                  alt="User"
                  width="30"
                  height="30"
                />
                Admin User
              </a>
              <div className="dropdown-menu dropdown-menu-right">
                <a className="dropdown-item" href="#">
                  Profile
                </a>
                <a className="dropdown-item" href="#">
                  Settings
                </a>
                <div className="dropdown-divider"></div>
                <a className="dropdown-item" href="#">
                  Logout
                </a>
              </div>
            </li>
          </ul>
        </div>
      </nav>

      {/* Sidebar and Main Content */}
      <div className="container-fluid">
        <div className="row">
          {/* Sidebar */}
          <nav id="sidebar" className="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
            <div className="sidebar-sticky pt-3">
              <ul className="nav flex-column">
                <li className="nav-item">
                  <a className="nav-link" href="#">
                    <i className="fa fa-tachometer-alt mr-2"></i>
                    Dashboard
                  </a>
                </li>
                <li className="nav-item">
                  <a className="nav-link active" href="#">
                    <i className="fa fa-users mr-2"></i>
                    Distributors
                  </a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#">
                    <i className="fa fa-user-plus mr-2"></i>
                    Add Distributor
                  </a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#">
                    <i className="fa fa-chart-bar mr-2"></i>
                    Reports
                  </a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#">
                    <i className="fa fa-cog mr-2"></i>
                    Settings
                  </a>
                </li>
              </ul>
            </div>
          </nav>

          {/* Main Content */}
          <main role="main" className="col-md-9 ml-sm-auto col-lg-10 px-md-4">
            <div className="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
              <h1 className="h2">Distributors</h1>
              <button type="button" className="btn btn-primary" onClick={handleOpenModal}>
                Add Distributor
              </button>
            </div>

            {/* Distributor List Card */}
            <div className="card mb-4">
              <div className="card-header">
                <h5 className="card-title mb-0">Distributor List</h5>
              </div>
              <div className="card-body">
                {/* Search Bar */}
                <div className="row mb-3">
                  <div className="col-md-6">
                    <div className="input-group">
                      <input type="text" className="form-control" placeholder="Search distributors..." />
                      <div className="input-group-append">
                        <button className="btn btn-outline-secondary" type="button">
                          <i className="fa fa-search"></i>
                        </button>
                      </div>
                    </div>
                  </div>
                </div>

                {/* Distributor Table */}
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
                      <tr>
                        <td>1</td>
                        <td>ABC Distributors</td>
                        <td>(555) 123-4567</td>
                        <td>123 Main St, New York, NY 10001</td>
                        <td>North East</td>
                        <td>
                          <span className="badge badge-success">Active</span>
                        </td>
                        <td>
                          <button className="btn btn-sm btn-info mr-1">
                            <i className="fa fa-edit"></i> Edit
                          </button>
                          <button className="btn btn-sm btn-danger">
                            <i className="fa fa-trash"></i> Delete
                          </button>
                        </td>
                      </tr>
                      <tr>
                        <td>2</td>
                        <td>XYZ Supply Co.</td>
                        <td>(555) 987-6543</td>
                        <td>456 Market St, San Francisco, CA 94103</td>
                        <td>West Coast</td>
                        <td>
                          <span className="badge badge-success">Active</span>
                        </td>
                        <td>
                          <button className="btn btn-sm btn-info mr-1">
                            <i className="fa fa-edit"></i> Edit
                          </button>
                          <button className="btn btn-sm btn-danger">
                            <i className="fa fa-trash"></i> Delete
                          </button>
                        </td>
                      </tr>
                      <tr>
                        <td>3</td>
                        <td>Midwest Distributors Inc.</td>
                        <td>(555) 456-7890</td>
                        <td>789 Oak Ave, Chicago, IL 60611</td>
                        <td>Midwest</td>
                        <td>
                          <span className="badge badge-danger">Inactive</span>
                        </td>
                        <td>
                          <button className="btn btn-sm btn-info mr-1">
                            <i className="fa fa-edit"></i> Edit
                          </button>
                          <button className="btn btn-sm btn-danger">
                            <i className="fa fa-trash"></i> Delete
                          </button>
                        </td>
                      </tr>
                      <tr>
                        <td>4</td>
                        <td>Southern Partners LLC</td>
                        <td>(555) 234-5678</td>
                        <td>321 Peachtree St, Atlanta, GA 30303</td>
                        <td>South East</td>
                        <td>
                          <span className="badge badge-success">Active</span>
                        </td>
                        <td>
                          <button className="btn btn-sm btn-info mr-1">
                            <i className="fa fa-edit"></i> Edit
                          </button>
                          <button className="btn btn-sm btn-danger">
                            <i className="fa fa-trash"></i> Delete
                          </button>
                        </td>
                      </tr>
                      <tr>
                        <td>5</td>
                        <td>Pacific Northwest Supply</td>
                        <td>(555) 876-5432</td>
                        <td>654 Pine St, Seattle, WA 98101</td>
                        <td>Northwest</td>
                        <td>
                          <span className="badge badge-success">Active</span>
                        </td>
                        <td>
                          <button className="btn btn-sm btn-info mr-1">
                            <i className="fa fa-edit"></i> Edit
                          </button>
                          <button className="btn btn-sm btn-danger">
                            <i className="fa fa-trash"></i> Delete
                          </button>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                {/* Pagination */}
                <nav aria-label="Distributor pagination">
                  <ul className="pagination justify-content-center">
                    <li className="page-item disabled">
                      <a className="page-link" href="#" tabIndex={-1}>
                        Previous
                      </a>
                    </li>
                    <li className="page-item active">
                      <a className="page-link" href="#">
                        1
                      </a>
                    </li>
                    <li className="page-item">
                      <a className="page-link" href="#">
                        2
                      </a>
                    </li>
                    <li className="page-item">
                      <a className="page-link" href="#">
                        3
                      </a>
                    </li>
                    <li className="page-item">
                      <a className="page-link" href="#">
                        Next
                      </a>
                    </li>
                  </ul>
                </nav>
              </div>
            </div>
          </main>
        </div>
      </div>

      {/* Add Distributor Modal - Using React state to control visibility */}
      {showModal && (
        <div className="modal fade show" style={{ display: "block" }} tabIndex={-1} role="dialog">
          <div className="modal-dialog" role="document">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">Add Distributor</h5>
                <button type="button" className="close" onClick={handleCloseModal}>
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div className="modal-body">
                <form id="addDistributorForm">
                  <div className="form-group">
                    <label htmlFor="distributorName">Name</label>
                    <input
                      type="text"
                      className="form-control"
                      id="distributorName"
                      placeholder="Enter distributor name"
                      required
                    />
                  </div>
                  <div className="form-group">
                    <label htmlFor="distributorPhone">Phone</label>
                    <input
                      type="text"
                      className="form-control"
                      id="distributorPhone"
                      placeholder="Enter phone number"
                      required
                    />
                  </div>
                  <div className="form-group">
                    <label htmlFor="distributorAddress">Address</label>
                    <textarea
                      className="form-control"
                      id="distributorAddress"
                      rows={3}
                      placeholder="Enter full address"
                      required
                    ></textarea>
                  </div>
                  <div className="form-group">
                    <label htmlFor="distributorRegion">Region</label>
                    <select className="form-control" id="distributorRegion" required>
                      <option value="">Select a region</option>
                      <option value="North East">North East</option>
                      <option value="South East">South East</option>
                      <option value="Midwest">Midwest</option>
                      <option value="Southwest">Southwest</option>
                      <option value="West Coast">West Coast</option>
                      <option value="Northwest">Northwest</option>
                    </select>
                  </div>
                  <div className="form-group">
                    <label>Status</label>
                    <div className="form-check">
                      <input
                        className="form-check-input"
                        type="radio"
                        name="distributorStatus"
                        id="statusActive"
                        value="Active"
                        defaultChecked
                      />
                      <label className="form-check-label" htmlFor="statusActive">
                        Active
                      </label>
                    </div>
                    <div className="form-check">
                      <input
                        className="form-check-input"
                        type="radio"
                        name="distributorStatus"
                        id="statusInactive"
                        value="Inactive"
                      />
                      <label className="form-check-label" htmlFor="statusInactive">
                        Inactive
                      </label>
                    </div>
                  </div>
                </form>
              </div>
              <div className="modal-footer">
                <button type="button" className="btn btn-secondary" onClick={handleCloseModal}>
                  Cancel
                </button>
                <button type="submit" form="addDistributorForm" className="btn btn-primary">
                  Save Distributor
                </button>
              </div>
            </div>
          </div>
          <div className="modal-backdrop fade show"></div>
        </div>
      )}
    </div>
  )
}
