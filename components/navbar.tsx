import Image from "next/image"

export function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-white border-bottom">
      <button className="navbar-toggler d-md-none" type="button" data-toggle="collapse" data-target="#sidebarMenu">
        <span className="navbar-toggler-icon"></span>
      </button>

      <a className="navbar-brand ml-2" href="#">
        <Image
          src="/placeholder.svg?height=30&width=120"
          alt="Company Logo"
          width={120}
          height={30}
          className="d-inline-block align-top"
        />
      </a>

      <div className="collapse navbar-collapse" id="navbarSupportedContent">
        <ul className="navbar-nav ml-auto">
          <li className="nav-item dropdown">
            <a
              className="nav-link dropdown-toggle"
              href="#"
              id="navbarDropdown"
              role="button"
              data-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            >
              <Image
                src="/placeholder.svg?height=30&width=30"
                alt="User Avatar"
                width={30}
                height={30}
                className="rounded-circle mr-2"
              />
              Admin User
            </a>
            <div className="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdown">
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
  )
}
