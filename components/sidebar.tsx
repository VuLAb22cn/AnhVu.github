export function Sidebar() {
  return (
    <div className="bg-light border-right" id="sidebar-wrapper">
      <div className="sidebar-heading border-bottom bg-white">Distributor Management</div>
      <div className="list-group list-group-flush collapse d-md-block" id="sidebarMenu">
        <a href="#" className="list-group-item list-group-item-action bg-light active">
          <i className="fas fa-tachometer-alt mr-2"></i> Dashboard
        </a>
        <a href="#" className="list-group-item list-group-item-action bg-light">
          <i className="fas fa-users mr-2"></i> Distributors
        </a>
        <a href="#" className="list-group-item list-group-item-action bg-light">
          <i className="fas fa-box mr-2"></i> Products
        </a>
        <a href="#" className="list-group-item list-group-item-action bg-light">
          <i className="fas fa-shopping-cart mr-2"></i> Orders
        </a>
        <a href="#" className="list-group-item list-group-item-action bg-light">
          <i className="fas fa-chart-bar mr-2"></i> Reports
        </a>
        <a href="#" className="list-group-item list-group-item-action bg-light">
          <i className="fas fa-cog mr-2"></i> Settings
        </a>
      </div>
    </div>
  )
}
